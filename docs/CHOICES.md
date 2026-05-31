# CHOICES.md

## 1. Detection Model Choice

Options Considered:
- YOLOv8n
- YOLOv8s
- RT-DETR

AI Suggestion:
Use YOLOv8 because it provides a strong balance between speed and accuracy for CCTV analytics.

Decision:
YOLOv8n was selected because it is lightweight, fast to run on local hardware, and sufficient for person detection in store CCTV footage.

---

## 2. Event Schema Design

Options Considered:
- Raw detections only
- Session-based event schema
- Behavioural event schema

AI Suggestion:
Use behavioural events rather than raw detections.

Decision:
Implemented structured events such as ENTRY, ZONE_ENTER, ZONE_DWELL and BILLING_QUEUE_JOIN to make downstream analytics easier and reduce coupling between detection and analytics layers.

---

## 3. API Architecture Choice

Options Considered:
- Monolithic script
- Flask
- FastAPI

AI Suggestion:
Use FastAPI due to automatic OpenAPI documentation and validation.

Decision:
FastAPI was selected because it provides strong typing, schema validation, automatic documentation, and production readiness.