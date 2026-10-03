# Optional: uv sync --extra aws. Requires your own approved AWS identity.
import os
import boto3
if __name__ == '__main__':
    session=boto3.Session(profile_name=os.getenv('AWS_PROFILE'),
                          region_name=os.environ['AWS_REGION'])
    client=session.client('bedrock-runtime')
    response=client.converse(modelId=os.environ['BEDROCK_MODEL_ID'],
        messages=[{'role':'user','content':[{'text':'Summarize: retrieval supplies external evidence.'}]}],
        inferenceConfig={'maxTokens':128})
    print(response['output']['message']['content'])
    print(response.get('usage',{}))
