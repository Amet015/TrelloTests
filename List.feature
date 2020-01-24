# Created by AlanEscalera at 1/21/2020
Feature: CRU of List

  Background: Insert the link https://api.trello.com/1/lists
    Given create a POST request to /boards/
    And sets the following Query Params
      """
        {
         "name":"testboard1"
        }
      """
    When Sends the Post
    Then should return a 200 status code as response
    And should show the next JSON
    """
      {
      "id": "{idBoard}",
      "name": "testboard1",
      "url": "https://trello.com/b/{id}/testboard1"
      }
    """
    And Save the JSON response as BoardObject
    And sets the authorization fields on postman



  Scenario: Creates a new list
    Given Sets a POST request to /lists/
    And sets the following Path Params
       """
          {
           "name":"newlisttest"
           "idBoard": "{BoardObject.id}"
          }
        """
    When Sends a Post to create a new list
    Then should return a 200 status code as response
    And should show the next JSON
         """
         {
          "id": "{idList}",
          "name": "newlisttest",
          "idBoard": "{idBoard}"
          }
         """
    And Save the JSON response as ListObject


  Scenario: Gets a list
    Given Has a List Created
    And sets a GET request to /lists/:id
    And sets the following Path Params
        """
          {
           "id": "{ListObject.id}"
          }
        """
    When Sends a Gets to get the list
    Then should return a 200 status code as response
    And should show the next JSON
         """
         {
          "id": "{idList}",
          "name": "newlisttest",
          "idBoard": "{idBoard}"
          }
         """


  Scenario: Edit the name of a list
    Given Has a List Created
    And sets a PUT request to /lists/:id
    And sets the following Path Params
        """
          {
            "id": "{ListObject.id}",
          "name": "nameUpdatedliste",
          }
        """
    When Sends a Gets to get the list
    Then should return a 200 status code as response
    And should show the next JSON
         """
         {
          "id": "{idList}",
          "name": "nameUpdatedliste",
          "idBoard": "{idBoard}",
          }
         """
    And Sends a DELETE request to /boards/:id
        """
        {
          "id": "{BoardObject.id}"
        }
        """
