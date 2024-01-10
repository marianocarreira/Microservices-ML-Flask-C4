# Microservice architecture and Machine Learning example using Python Flask and TensorFlow

## Author

Mariano Carreira

## Summary

This solution was developed within the framework of the "Software Engineering Topics 2" course in the Master's in Software Engineering program at the University of La Plata during the second semester of 2024. Successful completion of this project is a prerequisite for passing the course.

## Requirements

### Machine Learning


### Functional

The functional requirements were outlined by the professors and are detailed [here] [link]. In essence, the project entails creating a machine learning model capable of predicting cardiac risk based on specific parameters. Architecturally, the system is required to be built using a microservices architecture, leveraging the knowledge acquired in the course.

### Non-functional

Although no functional requirements were explicitly provided, an architecture is sought that exhibits responsive performance and demonstrates close scalability. Most design and architecture decisions stem from topics covered in class.

### Technologies

For the machine learning model, the proposed technologies include Python, Numpy, Keras, and TensorFlow. <br>
Python and Flask are recommended for implementing the additional requested services. <br>
Docker was proposed for deployment.

### Documentation

Comprehensive documentation, encompassing architecture and design decisions, is also a key requirement.<br>
This work includes the creation of Architectural Decision Records (ADRs), Sequence Diagrams, and Diagrams using Domain-Driven Design (DDD) principles.

## Solution Implemented

### Functional requeriments

### Non-Functional requeriments

## Architecture

The architecture was overdimensioned to some extent to comprehensively address the topics covered in class.

### ADRs

The ADR template was taken from: (link)

- [ADR00-RestFull-API](/documentation/architecture/ADRs/ADR00-RestFull-API.md)
- [ADR01-Microservicios-Style](/documentation/architecture/ADRs/ADR01-Microservicios-Style.md)
- [ADR02-RabbitMq](/documentation/architecture/ADRs/ADR02-RabbitMq.md)
- [ADR03-Contenerizacion-Docker](/documentation/architecture/ADRs/ADR03-Contenerizacion-Docker.md)
- [ADR04-AppGateway-pattern](/documentation/architecture/ADRs/ADR04-AppGateway-pattern.md)
- [ADR05_Flask_FlaskORM](/documentation/architecture/ADRs/ADR05_Flask_FlaskORM.md)

### Architecture Views

The selected diagram model is C4 Model (https://c4model.com/), created by Simon Brown (link to Simon's profile). <br>
For more details, please refer to the documentation available [here](add the C4 website link). <br>

Note: Componetns and Code diagram's level were meged into a single document.

#### System's Level

- [V01-C4_System-context-view](/documentation/architecture/views/V01-C4_System-context-view.md)

#### Containers' Level

- [V02-C4_Containers-all-view](./documentation/architecture/views/V02-C4_Containers-all-view.md)
- [V03-C4_Containers-ApiGateway-view](/documentation/architecture/views/V03-C4_Containers-ApiGateway-view.md)
- [V04-C4_Containers-Queue-view](/documentation/architecture/views/V04-C4_Containers-Queue-view.md)
- [V05-C4_Containers-PredictionsMs-view](/documentation/architecture/views/V05-C4_Containers-PredictionsMs-view.md)
- [V06-C4_Containers-UsersMs-view](/documentation/architecture/views/V06-C4_Containers-UsersMs-view.md)


#### Components' and Code's Level

- [V07-C4_Component-ApiGateway-view](/documentation/architecture/views/V07-C4_Component-ApiGateway-view.md)
- [V08-C4_Component-UsersMs-view](/documentation/architecture/views/V08-C4_Component-UsersMs-view.md)
- [V09-C4_Component-LoggingMs-view](/documentation/architecture/views/V09-C4_Component-LoggingMs-view.md)
- [V10-C4_Component-PredictionsMs-view](/documentation/architecture/views/V10-C4_Component-PredictionsMs-view.md)

### instructions to run the solution
