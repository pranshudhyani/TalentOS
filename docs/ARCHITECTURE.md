# Architecture Overview - TalentOS

## System Components
1. **API Gateway / Nginx**: Handles reverse proxying, rate limiting, and SSL.
2. **FastAPI Backend**: Handles domain logic, data models, and REST routing.
3. **Database Layer**: PostgreSQL for relational storage, Redis for async task queues.
4. **Vector Store**: Qdrant / Pinecone for vector embedding similarity queries.
