pm.test('Status code is 200 and content type is JSON', function () {
    pm.response.to.have.status(200);
    pm.response.to.have.jsonBody();
})

pm.test('Response time is lower 1s', function () {
    pm.expect(pm.response.responseTime).to.be.below(1000);
})

tests["verify country"] = responseBody.has(data.country)
tests["verify postal code"] = responseBody.has(data["post code"])
tests["verify place name"] = responseBody.has(data["place name"])

pm.test('Place name for each country and postal code', function () {
    const jsonData = pm.response.json();
    const place = jsonData.find(country => country["country"] === "{{country}}");
    pm.expect(place["post code"]).to.eql("{{postal-code}}");
    pm.expect(place["place name"]).to.eql("{{place name}}");
})