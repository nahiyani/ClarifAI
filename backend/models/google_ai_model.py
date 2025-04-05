from google.cloud import aiplatform

aiplatform.init(project='107470836018816573840', location='us-central1')

def summarize_with_google_ai(text):

    endpoint = "projects/clarifai-455717/locations/us-central1/endpoints/your-endpoint-id"

    try:
        response = aiplatform.gapic.PredictionServiceClient().predict(
            endpoint=endpoint,
            instances=[{"content": text}],
            parameters={"temperature": 0.2},
        )

        summary = response.predictions[0]
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None