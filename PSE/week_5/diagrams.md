Online Paid Table Booking System:

The Restaurant owner wants to provide an online booking table feature to its customer across their multiple branches.  

**As a customer I should be able to m**ake online bookings and payments.

As a r**estaurant staff I should be able to** manages table availability and confirms attendance of the booked customers in their branches.

**As an admin I should be able m**anage restaurant branches, tables, users, and generate reports.

![image.png](attachment:3698e86b-8517-4407-a339-e9e68a1ec431:image.png)

Use Case Description:

| use case name | Book Table |
| --- | --- |
| Scenario | book restaurunt table |
| Triggering event | customer wants to book a new table in advance |
| Brief description | online customers logs into the system and selects a restaurant, choose date/time, number of guests, and select available table |
| Actors | Customer |
| Related use cases | search resturants, make payments, view Booking history |
| Stakeholders | Customers, Restaurant Management, Finance Department |
| Preconditions | Customer must be registered and logged in, restaurant and table availability must be maintained and updated in the system, payment gateway must be accessible. |
| Postconditions | Table is booked and reserved in the system, payment is complete and logged, booking details are confirmed and shared with customers and staff. |
| Flow of activities | [https://www.notion.so/PSE-1f54a75baeaa804996fdf235fb659f92?pvs=4#1f54a75baeaa801c9974f3ff5e2265a0](https://www.notion.so/PSE-1f54a75baeaa804996fdf235fb659f92?pvs=21) |
| Exception conditions | User not logged in, No tables available for the selected time or location, payment gatway not working, payment failed or card declined. |

| Actor | System |
| --- | --- |
| customer logs in and goes to the booking section | system verifies login and displays restaurants options |
| customer selects restaurant, date, time, number of guests | System displays available tables for the selection. |
| Customer selects preferred table | System reservers the table temporarily |
| customer proceeds to payment | System initiates payment request via payment gateway |
| customer provides payment details and confirms payment | System processes the payment, confirms the booking, send confirmation via email/sms. |


## Class Diagram:
Please click the link: https://www.mermaidchart.com/play#pako:eNqNUMsKwjAQ_JWSkyL-gHipehFEsOrNy9qstdgkkoce1H83blCSWsEcAju7OzM7N1YqjmzEygaMmdVQaRA7mflHSLY1qLNbQF5vMOdRsQSBUVmoJi4rtC-k1w_YYydj5gKNBadB2on_yuPfKgtVgq2VjKAN7Bs0EbC2cDiYTl2a_VtsbiZKnTCeWDl02KKmmMb34TAj5TY4dcYqgbqN51zUMrVH-4m9EE9i0g_WlUT-dbePPE96P8J_G0qF6FLaS9Q8adL6wUnHJITA-RKvwf97iRoahbpgR8OdOdiuRqCicD7y7PEE00THjQ

User

- Id

- Name

- Role

- getRole()

Restaurant Branch

- Id

- Name

- Location

- Tables

- Staffs

Table

- Id

- Name

- IsBooked

- Queue

Staff → extends User

- BranchId

- assignedTables

- getAssignedTables()

Customer → extends User

- BookedTableId

- getBookedTableId()

Admin → extends User

- addNewBranch()

- removeBranch()

- updateBranch()

- addNewStaff()