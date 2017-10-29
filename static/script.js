function attach_issue_to_chat() {
    $('.ind .ind-name').click(function(e) {
        let name = e.target.innerText;

        let comment_id = e.target.nextElementSibling.innerText;
        console.log(comment_id );
        document.forms[0].comment_id.value = comment_id;

        $('.chatbox .chat-msg-container').text('');
        $('.chatbox .chat-name').text(name);
        $('.chatbox').css({'display': 'block'});
        document.forms[0].comment_id.value = '';

        $.ajax({
            url: '/helpdesk/chat/get/',
            data: {q: comment_id},
            success: function(data) {
                $('.chat-msg-container').text('');

                for (let i = 0; i < data.length; i++) {
                    let classname = (data[i].from_name == 'expedite.ai') ? 'reply' : 'issue';
                    let newhtml = '<div class="' + classname + '">' + data[i].message + '</div>';
                    $('.chat-msg-container').append(newhtml);

                }

            }
        });
    });
}


function handle_chat_submit() {
    $('#chat-form').submit((e) => {
        e.preventDefault();
        let message = document.forms[0].message.value;
        let comment_id = document.forms[0].comment_id.value;
        let newhtml = '<div class="reply">' + message + '</div>';
        $('.chat-msg-container').append(newhtml);

        $.ajax({
            method:'POST',
            url: '/facebook/comment_on_fb/',
            data: {
                comment_id: comment_id,
                message: message
            },
            success: (data) => {
                console.log(data);
                document.forms[0].comment_id.value = '';
            }
        });
    });
}


$(document).ready(() => {
    attach_issue_to_chat();
    handle_chat_submit();
});
