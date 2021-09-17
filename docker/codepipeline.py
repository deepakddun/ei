import boto3

client = boto3.client('codepipeline', region_name='us-east-2')

res = client.put_approval_result(
							pipelineName= 'SampleManualApprovalPipeline',
							stageName='ManualApproval',
							actionName='ApproveOrDeny',
							result={'summary':'Rejected','status':'Rejected'},
							token='90ce650c-6510-41aa-b443-730a5b263a31')

print(res)