workspace {
    
    !identifiers hierarchical
    
    model {
        internal_user = person "Internal User"
        external_user = person "External User"
    
        softwareSystem = softwareSystem "Sistema de Riesgo Cardiaco" {

            apiGatewayMs = group "t2_tp_gategay_ms" {
                apiGatewayMsApi = container "API Gateway" {
                    tags "ApiGateway" "Service API"
                    authMiddleware = component "Auth Middleware" "Authenticate users before any other action"
                    loggingMiddlewareBefore = component "Logging Middleware Before" "Meassure the request calls in Sec." "Queue log information about the request"
                    loggingMiddlewareAfter = component "Logging Middleware After"
                    rateLimitingMiddleware = component "Rate limiting Middleware" "Control the requests number by user's Subscription"
                    router = component "Router" "Authenticate users before any other action"
                    logProducer = component "Logs_Producer" "Publishes log messages to the queue"
                }
                cache = container "Simple Cache" {
                    tags "ApiGateway" "Database"
                    apiGatewayMsApi -> this "Lee/Escribe"
                }
            }

            usersMs = group "t2_tp_users_ms" {
                usersMsApi = container "Users-MS" {
                    tags "UsersMS" "Service API"
                    group "Api" {
                         controller = component "Controller" "Handle requests, validate parameters and call services"    
                    }
                    group "Domain" {
                         service = component "Service" "Service that contains business logic"
                    }
                    group "Infrastructure" {
                         model = component "Repository" "Object model and repository at same time (ORM)"
                         config = component "Configuration" "Configuration manager"
                         seeder = component "DbSeeder" "Database Seeder"
                    }
                }
                usersdb = container "UsersMS Database" {
                    tags "UsersMS" "Database"
                    usersMsApi -> this "Reads from and writes to"
                }
            }

            queue = group "RabbitMQ" {
                queueApi = container "queue-log" {
                    tags "RabbitMQTag"
                    subs = component "Subcribers"
                }
            }

            loggingMs = group "t2_tp_logging_ms" {
                loggingMsApi = container "Logging-MS" {
                    tags "LoggingMS" "Service API"
                    group "Api" {
                         controller = component "Controller" "Handle requests, validate parameters and call services"    
                    }
                    group "Domain" {
                         service = component "Service" "Service that contains business logic"
                    }
                    group "Infrastructure" {
                         model = component "Repository" "Object model and repository at same time (ORM)"
                         config = component "Configuration" "Configuration manager"
                         loggerConsumer = component "QueueConsumer" "Listen the Logs Queue"
                    }
                }
                loggingDb = container "logging-db" {
                    tags "LoggingMS" "Database"
                    loggingMsApi -> this "Reads from and writes to"
                }
            }

            predictionsMs = group "t2_tp_predictions_ms" {
                predictionsMsApi = container "Predictions-MS" {
                    tags "PredictionsMS" "Service API"
                    group "Api" {
                         controller = component "Controller" "Handle requests, validate parameters and call services"    
                    }
                    group "Domain" {
                         service = component "Service that contains business logic"
                    }
                    group "Infrastructure" {
                         mlModel = component "Riesgo_cardiaco_model_v1" "Predict cardiac risk"
                         config = component "Configuration manager"
                    }
                }
            }

            internal_user -> softwareSystem "Gestiona"
            external_user -> softwareSystem "Consulta"
            External_user -> apiGatewayMsApi "Consulta"
            internal_user -> usersMsApi "Gestiona (PostMan)"
            internal_user -> loggingMsApi "Consulta (PostMan)"
            apiGatewayMsApi -> predictionsMsApi "(2) Consulta Predicción"
            apiGatewayMsApi -> usersMsApi "(1) Autentica"
            apiGatewayMsApi -> queueApi "(3) Publica LogEntry"
            queueApi -> loggingMsApi "Subscribe LogEntry"
            external_user -> apiGatewayMsApi.authMiddleware
            
            apiGatewayMsApi.authMiddleware -> apiGatewayMsApi.rateLimitingMiddleware "User's Info"
            apiGatewayMsApi.authMiddleware -> softwareSystem.usersMsApi "Authenticates"
            apiGatewayMsApi.rateLimitingMiddleware -> apiGatewayMsApi.loggingMiddlewareBefore
            apiGatewayMsApi.loggingMiddlewareBefore -> apiGatewayMsApi.router "Start Tracing"
            apiGatewayMsApi.router -> apiGatewayMsApi.loggingMiddlewareAfter
            apiGatewayMsApi.loggingMiddlewareAfter -> apiGatewayMsApi.logProducer
            apiGatewayMsApi.router -> softwareSystem.predictionsMsApi "End Tracing"
            apiGatewayMsApi.rateLimitingMiddleware -> softwareSystem.cache
            apiGatewayMsApi.logProducer -> queueApi "Publish log entry"
            
            apiGatewayMsApi -> usersMsApi.controller "Authentication"
            internal_user -> usersMsApi.controller "Manages users"
            usersMsApi.controller -> usersMsApi.service
            usersMsApi.service -> usersMsApi.model
            usersMsApi.model -> usersdb
            usersMsApi.seeder -> usersdb "Seeds"
            
            internal_user -> loggingMsApi.controller "Query logs"
            loggingMsApi.controller -> loggingMsApi.service
            loggingMsApi.service -> loggingMsApi.model
            loggingMsApi.model -> loggingDb
            queueApi -> loggingMsApi.loggerConsumer "Listen"
            
            apiGatewayMsApi -> predictionsMsApi.controller
            predictionsMsApi.controller -> predictionsMsApi.service
            predictionsMsApi.service -> predictionsMsApi.mlModel
        }

    }
    
    views {
        component softwareSystem.apiGatewayMsApi {
            include *
            autolayout
        }
        
        component softwareSystem.usersMsApi {
            include *
            autolayout
        }
        
        component softwareSystem.loggingMsApi {
            include *
            autolayout
        }
        
        component softwareSystem.predictionsMsApi {
            include *
            autolayout
        }
        
        systemLandscape softwareSystem "Heart Risk System" {
            include *
            autolayout
        }
        
        container softwareSystem "Containers_All" {
            include *
            autolayout
        }

        container softwareSystem "Containers_apiGatewayMs" {
            include ->softwareSystem.apiGatewayMs->
            autolayout
        }

        container softwareSystem "Containers_usersMs" {
            include ->softwareSystem.usersMs->
            autolayout
        }

        container softwareSystem "Containers_predictionsMs" {
            include ->softwareSystem.predictionsMs->
            autolayout
        }
        
        container softwareSystem "Containers_loggingMs" {
            include ->softwareSystem.loggingMs->
            autolayout
        }
        
        container softwareSystem "Containers_queue" {
            include ->softwareSystem.queue->
            autolayout
        }
        
        styles {
            element "Person" {
                shape Person
            }
            element "Service API" {
                shape hexagon
            }
            element "Database" {
                shape cylinder
            }
            element "ApiGateway" {
                background #91F0AE
            }
            element "UsersMS" {
                background #e18cf0
            }
            element "RabbitMQTag" {
                shape Pipe
            }
            element "RabbitMQTag" {
                background #8CD0F0
            }
            element "LoggingMS" {
                background #F08CA4
            }
            element "PredictionsMS" {
                background #FFAC33
            }
            element "Service 6" {
                background #DD8BFE
            }
            element "Service 7" {
                background #89ACFF
            }
            element "Service 8" {
                background #FDA9F4
            }
            
        }

    }

}