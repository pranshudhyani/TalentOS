from fastapi import FastAPI

app = FastAPI(
    title="TalentOS API Engine",
    version="0.1.0",
    description="Backend API services for TalentOS AI Platform"
)


@app.get("/")
def read_root():
    return {"status": "online", "system": "TalentOS Engine", "version": "0.1.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
