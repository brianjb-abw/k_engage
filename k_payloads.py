

k_payloads = {
    "get_token":
    {
        "query": """
            mutation($clientId: String, $secretKey: String) {
                createSessionToken(clientId: $clientId, secretKey: $secretKey)
            }
        """,
        "variables": {}
    },

    "card_list":
    {
        "query": """
            query {
                cards {
                    id
                    name
                    status
                    lastFour
                    expirationDate
                    media
                    lockState
                }
            }
        """,
        "variables": {}
    }

}