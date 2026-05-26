

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

    "get_bal":
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
            query {
                transactions {
                    id
                    transactionDate
                    card {id}
                    transactionStatus
                    transactionType
                    merchantName
                    amount
                    category {
                        id
                        name
                    }
                    mcc {
                        code
                        description
                        category
                    }
                    zipCode
                    streetAddress
                    city
                    state
                    merchantId
                    cardPresent
                    cardHolderPresent
                    entryMode
                    terminalType
                    terminalId
                    merchantLogo
                    mid
                    merchantOfficialPage
                    merchantPhoneNumber
                    cardAcceptorId
                }
            }
        """,
        "variables": {}
    }

}


    # "trx_list":
    # {
    #     "query": """
    #         query {
    #             transactions {
    #                 id
    #                 transactionDate
    #                 card {id}
    #                 transactionStatus
    #                 transactionType
    #                 merchantName
    #                 amount
    #                 category {
    #                     id
    #                     name
    #                 }
    #                 mcc {
    #                     code
    #                     description
    #                     category
    #                 }
    #                 zipCode
    #                 streetAddress
    #                 city
    #                 state
    #                 merchantId
    #                 cardPresent
    #                 cardHolderPresent
    #                 entryMode
    #                 terminalType
    #                 terminalId
    #                 merchantLogo
    #                 mid
    #                 merchantOfficialPage
    #                 merchantPhoneNumber
    #                 cardAcceptorId
    #             }
    #         }
    #     """,
    #     "variables": {}
    # }