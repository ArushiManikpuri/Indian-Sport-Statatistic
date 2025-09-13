# Sports Stats System - High Level Design (HLD)

## 1. Overview
The Sports Stats System is designed to manage players, teams, and match statistics. It exposes REST APIs for CRUD operations on `Player`, `Team`, and `Match` entities. The system is built for scalability, maintainability, and extensibility.

---

## 2. Key Features
- Player Management (CRUD APIs)
- Team Management (CRUD APIs)
- Match Statistics
- API Gateway for routing
- Database for persistent storage
- Caching layer for faster reads
- Monitoring & Logging

---

## 3. High Level Architecture

```mermaid
flowchart TD
    Client[Client Apps (Web/Mobile)] --> |REST API| API[API Gateway]
    API --> |Route| PlayerService[Player Service]
    API --> |Route| TeamService[Team Service]
    API --> |Route| MatchService[Match Service]

    PlayerService --> DB[(Database)]
    TeamService --> DB[(Database)]
    MatchService --> DB[(Database)]

    API --> Cache[(Redis Cache)]
    API --> Monitor[Monitoring/Logging]
```

---

## 4. API Endpoints

### Player CRUD APIs
- **Create Player** → `POST /api/v1/players`
- **Get Player by ID** → `GET /api/v1/players/{id}`
- **Update Player** → `PUT /api/v1/players/{id}`
- **Delete Player** → `DELETE /api/v1/players/{id}`
- **List Players** → `GET /api/v1/players`

### Team CRUD APIs
- **Create Team** → `POST /api/v1/teams`
- **Get Team by ID** → `GET /api/v1/teams/{id}`
- **Update Team** → `PUT /api/v1/teams/{id}`
- **Delete Team** → `DELETE /api/v1/teams/{id}`
- **List Teams** → `GET /api/v1/teams`

### Match CRUD APIs
- **Create Match** → `POST /api/v1/matches`
- **Get Match by ID** → `GET /api/v1/matches/{id}`
- **Update Match** → `PUT /api/v1/matches/{id}`
- **Delete Match** → `DELETE /api/v1/matches/{id}`
- **List Matches** → `GET /api/v1/matches`

---

## 5. Database Design (Simplified)
- **Players Table**
  - player_id (PK)
  - name
  - age
  - role
  - team_id (FK)

- **Teams Table**
  - team_id (PK)
  - name
  - coach
  - region

- **Matches Table**
  - match_id (PK)
  - team1_id (FK)
  - team2_id (FK)
  - score_team1
  - score_team2
  - match_date

---

## 6. Versioning & Backward Compatibility
- APIs use versioning like `/api/v1/players`
- New versions (v2, v3) can be added without breaking old clients
- Backward compatibility ensures existing users don’t need to change immediately when new APIs are released

---

## 7. Non-Functional Requirements
- **Scalability**: Load balancer, horizontal scaling
- **Performance**: Redis cache for frequently accessed data
- **Security**: Authentication & authorization
- **Monitoring**: Prometheus, Grafana, ELK
- **Reliability**: Replication, backups, retries
