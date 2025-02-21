# Speech Synthesis Service
## Purpose
Converts text into natural-sounding speech for voice interactions.

## Responsibilities
- Generate audio from text using local or cloud-based TTS models.
- Support voice output for NLP responses and chat interactions.

## Inputs
- Text from NLP Service (e.g., AI responses).
- Direct text from Custom Chat App.
- Context from Real-Time Data Sync (e.g., voice preferences).

## Outputs
- Audio files/streams to Custom Chat App or Real-Time Data Sync.
- Optional metadata (e.g., audio format).

## Technologies
- Python
- Azure Text-to-Speech (cloud), gTTS/Tacotron 2 (local)
- Firebase for real-time data
- REST (FastAPI) or gRPC for communication

## See Also
- ClickUp: Core Architecture > Tasks > "Define Microservice Boundaries"
- Full architecture: `/docs/microservices-design.md`