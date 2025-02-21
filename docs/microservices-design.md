# Microservices Design
## NLP Service
- **Purpose**: Natural language processing for AI interactions.
- **Inputs**: Text from audio/chat, Firebase context.
- **Outputs**: Text to speech/data sync/chat.
- **Tech**: Python, OpenAI, PyTorch, Firebase.
- **Status**: Defined on Feb 21, 2025. See `/services/nlp/`.

## Computer Vision Service
- **Purpose**: Image and video analysis with local/cloud models.
- **Inputs**: User uploads, Firebase context.
- **Outputs**: Analysis data to NLP/data sync/chat.
- **Tech**: Python, PyTorch, OpenVINO, Azure, Firebase.
- **Status**: Defined on Feb 21, 2025. See `/services/computer-vision/`.

## Audio Recognition Service
- **Purpose**: Speech-to-text conversion for voice inputs.
- **Inputs**: User audio, Firebase context.
- **Outputs**: Text to NLP/data sync/chat.
- **Tech**: Python, Azure Speech, Whisper, Firebase.
- **Status**: Defined on Feb 21, 2025. See `/services/audio-recognition/`.

