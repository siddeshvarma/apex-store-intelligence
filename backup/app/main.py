from fastapi import FastAPI
from fastapi import Depends
from app.metrics import calculate_metrics
from sqlalchemy.orm import Session
from app.funnel import calculate_funnel
from app.database import Base
from app.database import engine
from app.database import get_db
from app.heatmap import calculate_heatmap
from app.models import EventSchema
from app.models import EventTable
from app.anomalies import get_anomalies
from app.ingestion import save_event

from app.health import get_health

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Store Intelligence API"
)


@app.get("/")
def root():
    return {
        "message": "Store Intelligence API Running"
    }


@app.get("/health")
def health():
    return get_health()


@app.post("/events/ingest")
def ingest_events(
    events: list[EventSchema],
    db: Session = Depends(get_db)
):

    inserted = 0
    duplicates = 0

    for event in events:

        result = save_event(db, event)

        if result:
            inserted += 1
        else:
            duplicates += 1

    return {
        "inserted": inserted,
        "duplicates": duplicates
    }
@app.get("/stores/{store_id}/metrics")
def metrics(
    store_id: str,
    db: Session = Depends(get_db)
):
    return calculate_metrics(db, store_id)
@app.get("/stores/{store_id}/funnel")
def funnel(
    store_id: str,
    db: Session = Depends(get_db)
):
    return calculate_funnel(db, store_id)
@app.get("/stores/{store_id}/heatmap")
def heatmap(
    store_id: str,
    db: Session = Depends(get_db)
):
    return calculate_heatmap(db, store_id)
@app.get("/stores/{store_id}/anomalies")
def anomalies(
    store_id: str,
    db: Session = Depends(get_db)
):
    return get_anomalies(db, store_id)