# V09 Component - Logging Microservice
View and diagram based on [C4 Diagram Models](https://c4model.com/).

Component diagram shows how a container is made up of a number of components. <br>
Provides more details about the responsibilities and the technology/implementation details of components.
<br>

<img src="../diagrams/dark/structurizr-1-Component-003.png" alt="drawing" width="950"/>

## Element Catalog 

<img src="../diagrams/dark/structurizr-1-Component-003-key.png" alt="drawing" width="600"/>

#### Internal User
- Human being with a access to the VPN.

#### Controller
- Handles requests.
- Validates requests parameters.

#### Service
- Contains business logic.
- Business logic entry point.
- Acces to the Repository

#### Repository
- Access to the database. (read/write)
- Contains also the model objects.

#### Configuration
- Handles configuration.
- Configuration source depends on the environment its running.

#### Queue Consumer
- Manages Queue connection to the queue (RabbitMQ).
- Subscribes to the logging-queue.
- Receives LogEntries published to that queue.

## Behavior (C4 Code Level)
  - Commond Db acces to query logs

 <img src="../diagrams/sequence_uml/seq_commonflow_all_plantuml.png" alt="drawing" width="700"/>

   - Flow when a new log Entry is published

 <img src="../diagrams/sequence_uml/seq_loggingConsumer_plantuml.png" alt="drawing" width="500"/>

## Related ADRs 
- [ADR00-RestFull-API](/documentation/architecture/ADRs/ADR00-RestFull-API.md)
- [ADR01-Microservicios-Style](/documentation/architecture/ADRs/ADR01-Microservicios-Style.md)
- [ADR03-Contenerizacion-Docker](/documentation/architecture/ADRs/ADR03-Contenerizacion-Docker.md)
- [ADR04-AppGateway-pattern](/documentation/architecture/ADRs/ADR04-AppGateway-pattern.md)
- [ADR02-RabbitMq](/documentation/architecture/ADRs/ADR02-RabbitMq.md)
- [ADR05_Flask_FlaskORM](/documentation/architecture/ADRs/ADR05_Flask_FlaskORM.md)

## Related Views
- [V09-C4_Component-LoggingMs-view](./V09-C4_Component-LoggingMs-view.md)