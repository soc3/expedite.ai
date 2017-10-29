function attach_issue_to_chat() {
    $('.ind .ind-name').click(function(e) {
        let name = e.target.innerText;


        let comment_id = e.target.nextElementSibling.innerText;
        console.log(comment_id );

        $('.chatbox .chat-name').text(name);

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
                console.log(data);
            }
        });
    });
}


function handle_chat_submit() {
    $('#chat-form').submit((e) => {
        e.preventDefault();
        let newhtml = '<div class="reply">' + document.forms[0].message.value + '</div>';
        $('.chat-msg-container').append(newhtml);
    });
}


$(document).ready(() => {
    attach_issue_to_chat();
    handle_chat_submit();
});
