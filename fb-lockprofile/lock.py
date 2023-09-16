import requests

profile_id = ""

access_token = ""

url = "https://graph.facebook.com/v3.1/graphql?variables={\u00220\u0022:{\u0022is_shielded\u0022:true,\u0022actor_id\u0022:\u0022" + profile_id + "\u0022,\u0022client_mutation_id\u0022:\u0022b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0\u0022}}&doc_id=1477043292367183&access_token=" + access_token + "&method=post"

res = requests.post(url)

# off shield
# "https://graph.facebook.com/v3.1/graphql?variables={\u00220\u0022:{\u0022is_shielded\u0022:false,\u0022actor_id\u0022:\u0022" + id + "\u0022,\u0022client_mutation_id\u0022:\u0022b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0\u0022}}&doc_id=1477043292367183&access_token=" + w.access_token + "&method=POST"

print(res.status_code)
print(res.text)