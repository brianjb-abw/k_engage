

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

    "bal":
    {
        "query": """
            query {
                account {
                    revolvingLoan {
                        balance
                        limit

                    }
                }
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
    },

    "trx_list":
    {
        "query": """

        """
    }

}