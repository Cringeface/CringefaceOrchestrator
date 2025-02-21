# Audio Recognition Service
## Purpose
Converts spoken audio into text using speech-to-text models.

## Responsibilities
- Process audio files or streams into text.
- Support local (e.g., Whisper) and cloud (e.g., Azure Speech) models.
- Enable voice-based input for NLP and chat interactions.

## Inputs
- Audio files from users (via Custom Chat App).
- Real-time audio streams (future capability).
- Context from Real-Time Data Sync (Firebase).

## Outputs
- Text to NLP Service, Real-Time Data Sync, or Custom Chat App.

## Technologies
- Python
- Azure Speech Services (cloud), Whisper (local)
- Firebase for real-time data
- REST (FastAPI) or gRPC for communication

## See Also
- ClickUp: Core Architecture > Tasks > "Define Microservice Boundaries"
- Full architecture: `/docs/microservices-design.md`