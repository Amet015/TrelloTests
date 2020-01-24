# Created by AlanEscalera at 1/21/2020
Feature: CRUD of Board

  Scenario: Creates a new board
    Given Sets a POST request to "https://api.trello.com/1/boards/"
    And sets the "GherkinBoard" as name

    When Sends the Post
    Then should return a "200" status code as response
   # And should show the next JSON
    """
      {
      "name": "testboard1",
      "desc": "",
      "descData": null,
      "closed": false,
      "idOrganization": null,
      "idEnterprise": null,
      "pinned": false
      }
    """
    And sets a DELETE request to "https://api.trello.com/1/boards/"
    And sends the Delete request


