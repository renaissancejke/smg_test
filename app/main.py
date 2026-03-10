from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app import crud, models
from app.config import settings
from app.database import Base, engine, get_db
from app.schemas import ShortenRequest, ShortenResponse, StatsResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener",
    description="A simple URL shortening service",
    version="1.0.0",
)


@app.post("/shorten", response_model=ShortenResponse, status_code=201)
def shorten_url(payload: ShortenRequest, db: Session = Depends(get_db)):
    original_url = str(payload.url)
    link = crud.create_link(db, original_url=original_url)
    return ShortenResponse(
        short_id=link.short_id,
        short_url=f"{settings.BASE_URL}/{link.short_id}",
        original_url=link.original_url,
    )


@app.get("/stats/{short_id}", response_model=StatsResponse)
def get_stats(short_id: str, db: Session = Depends(get_db)):
    link = crud.get_link_by_short_id(db, short_id)
    if not link:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return StatsResponse(
        short_id=link.short_id,
        original_url=link.original_url,
        clicks=link.clicks,
        created_at=link.created_at,
    )


@app.get("/{short_id}")
def redirect(short_id: str, db: Session = Depends(get_db)):
    link = crud.get_link_by_short_id(db, short_id)
    if not link:
        raise HTTPException(status_code=404, detail="Short URL not found")
    crud.increment_clicks(db, link)
    return RedirectResponse(url=link.original_url, status_code=302)
