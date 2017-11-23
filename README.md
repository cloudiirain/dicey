http://stackoverflow.com/questions/21214270/flask-run-function-every-hour

http://forum.novelupdates.com/profile-posts/143542/comment

http://forum.novelupdates.com/login

http://chatterbot.readthedocs.io/en/stable/setup.html

http://forum.novelupdates.com/profile-posts/143542/comments

http://forum.novelupdates.com/profile-posts/143545/comments (spam length = 50)

http://forum.novelupdates.com/posts/1032837/like

http://forum.novelupdates.com/threads/dungeons-common-area.23248/reply?quote=1032837

BOT:
- SUBSCRIBE_PAGE



Variables to save:
- Current Page Number (Cached)
- Sqlite database
    - message_id
    - players

HANDLE_PAGE:
- Go to cached current page
- READ_MESSAGES
- Check if total number of pages == current page number (cached)
- If false:
    - Increment "current_page_cache"
    - HANDLE_PAGE

READ_MESSAGES:
- For each message
    - Check if message_id is in the database.
    - If message id doesn't exist, handle HANDLE_MESSAGE

HANDLE_MESSAGE
- Remove blockquotes
- CUSTOM_FUNCTION
- Add message_id to database

CUSTOM_FUNCTION
- Case: !register
    - Add username to database
    - Add 13 cards to this user
    - POST response
- Case: !status
    - Calculate the number of cards
    - POST response
- Case: !attack @username
    - Check if @username exists
    - PLAY_WAR
    - POST response
- Case: !ranking
    - POST response (player ranking and )
- Case: !quit
