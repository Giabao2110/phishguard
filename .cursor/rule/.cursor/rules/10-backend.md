# Backend Rule

Applies to: backend/**

Use:
- Java 17
- Maven
- Spring Boot
- Spring Security
- Spring Data JPA
- Thymeleaf
- PostgreSQL

Required package structure:
- controller
- service
- repository
- model
- dto
- config
- security

Rules:
- keep controllers thin
- put business logic in services
- validate request DTOs
- add error handling
- use clean naming
- do not introduce unnecessary abstractions
- do not convert frontend to React