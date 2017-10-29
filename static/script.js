function attach_issue_to_chat() {
    $('.ind .ind-name').click(function(e) {
        let name = e.target.innerText;


        let comment_id = e.target.nextElementSibling.innerText;
        console.log(comment_id );

        $('.chatbox .chat-name').text(name);


    });
}


$(document).ready(() => {
    attach_issue_to_chat();
});
