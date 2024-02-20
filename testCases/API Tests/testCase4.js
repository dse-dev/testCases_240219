pm.test('Status code is 200 and content type is JSON', function () {
    pm.response.to.have.status(200);
    pm.response.to.have.jsonBody();
})

pm.test('Response time is lower 1s', function () {
    pm.expect(pm.response.responseTime).to.be.below(1000);
})

pm.test('Country is Germany and state is Badem-Wuerttemberg', function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.country).to.eql('Germany');
    pm.expect(jsonData.state).to.eql('Baden-Württemberg');
})

pm.test("Place name Stuttgart Degerloch has post code 70597", function () {
    const jsonData = pm.response.json();
    const place = jsonData.places.find(place => place["place name"] === "Stuttgart Degerloch");
    pm.expect(place["post code"]).to.eql("70597");
    // sees the first of two place name elements with value Stuttgart Degerloch
    // which has post code value "70567"
    // the second "Stuttgart Degerloch" has post code value "70597"
});

