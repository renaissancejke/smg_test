from sqlalchemy.orm import Session

from app import models
from app.shortener import generate_short_id


def get_link_by_short_id(db: Session, short_id: str) -> models.Link | None:
    return db.query(models.Link).filter(models.Link.short_id == short_id).first()


def create_link(db: Session, original_url: str) -> models.Link:
    for _ in range(5):
        short_id = generate_short_id()
        if not get_link_by_short_id(db, short_id):
            break
    else:
        raise RuntimeError("Failed to generate a unique short_id after 5 attempts")

    link = models.Link(short_id=short_id, original_url=original_url)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


def increment_clicks(db: Session, link: models.Link) -> models.Link:
    link.clicks += 1
    db.commit()
    db.refresh(link)
    return link
