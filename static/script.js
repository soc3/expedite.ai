function attach_issue_to_chat() {
    $('.ind .ind-name').click(function(e) {
        let name = e.target.innerText;

        let comment_id = e.target.nextElementSibling.innerText;
        console.log(comment_id );
        document.forms[0].comment_id.value = comment_id;

        $('.chatbox .chat-msg-container').text('');
        $('.chatbox .chat-name').text(name);
        $('.chatbox').css({'display': 'block'});
        document.forms[0].message.value = '';

        $('.ind').removeClass('open');
        console.log(e.target);
        $(e.target).closest('ind').addClass('open');
        console.log($(e.target).closest('ind'));
        $(e.target.parentElement.parentElement).addClass('open');
        $('.ind .material-icons').hide();

        $(e.target.parentElement.parentElement).find('.material-icons').show();

        $.ajax({
            url: '/helpdesk/chat/get/',
            data: {q: comment_id},
            success: function(data) {
                $('.chat-msg-container').text('');

                for (let i = 0; i < data.length; i++) {
                    let classname = (data[i].from_name == 'expedite.ai') ? 'reply' : 'issue';
                    let newhtml = '<div class="' + classname + '">' + data[i].message + '</div>';
                    $('.chat-msg-container').append(newhtml);

                    $('.chat-msg-container').scrollTop($('.chat-msg-container')[0].scrollHeight);
                }

            }
        });
    });

    $('.ind .material-icons').click(function(e) {
        console.log(e.target);
        let comment_id = e.target.parentElement.parentElement.parentElement.getElementsByClassName('ind-id')[0].innerText;
        console.log(comment_id);
        let url = '';
        let node = e.target.parentElement.parentElement.parentElement;

        if ($(e.target).hasClass('done')) {
            url = '/helpdesk/issues/resolve';
        } else {
            url = '/helpdesk/issues/archive';
        }

        $.ajax({
            method: 'GET',
            url: url,
            data: {id: comment_id},
            success: function(data){
                console.log(data);
                node.style.display = 'none';
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
                document.forms[0].message.value = '';
            }
        });
    });
}


$(document).ready(() => {
    attach_issue_to_chat();
    handle_chat_submit();
    $('.ind .material-icons').hide();
});
