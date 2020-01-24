# Created by AlanEscalera at 1/21/2020
Feature: CRUD of Card

  Background: Insert the link https://api.trello.com/1/cards
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
    And sets the authorization fields on postman



  Scenario: Creates a new card
    Given sets a POST request to /cards/
    When Sends a Post to create a new card
        """
          {
           "idList":"{ListObject.id}"
          }
        """
    Then should return a 200 status code as response
    And should show the next Json
        """
        {
          "id": "{idCard}"
        }
        """
   And Save the JSON response as CardObject



  Scenario: Gets a card through Id
    Given Sets a GET request to /cards/:id
    And sets the following Path parameters
     """
        {
          "id": "{CardObject.id}"
        }
        """
    When sends the request
    Then should return a 200 status code as response
    And should show the next JSON
        """
        {
          "id": "{idCard}"
        }
        """


  Scenario: Edits a card through Id
    Given sets a PUT request to /cards/:id
        """
        {
          "id": "{CardObject.id}"
          "name":"CardUpdated"
        }
        """
    When sends the request
    Then should return a 200 status code as response
    And should show the next JSON
     """
        {
          "id": "{idCard}"
          "name":"CardUpdated"
        }
      """


  Scenario: Deletes a card
    Given sets a DELETE request to /cards/:id
    When Sends a Post to delete a card
        """
          {
           "id":"{CardObject.id}"
          }
        """
    Then should return a 200 status code as response
    And should show the next JSON
        """
        {
          "limits": {}
        }
        """
    And Sends a DELETE request to /boards/:id
        """
        {
          "id": "{BoardObject.id}"
        }
        """