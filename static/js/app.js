import { marked } from 'marked';
// Use marked as needed

class Chat{
    constructor() {
        this.args = {
            openButton: document.querySelector('.chat__button'),
            chatBox: document.querySelector('.chat__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chat) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chat.classList.add('chat--active')
        } else {
            chat.classList.remove('chat--active')
        }
    }

    onSendButton(chat) {
        var textField = chat.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(response => response.text())
          .then(responseText => {
              let msg2 = { name: "Mires", message: responseText };
              this.messages.push(msg2);
              this.updateChatText(chat);
              textField.value = '';
          })
        .catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chat)
            textField.value = ''
          });
    }

    updateChatText(chat) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            let messageHtml = marked(item.message);
            console.log(messageHtml)
            if (item.name === "Mires")
            {
                html += '<div class="messages__item messages__item--visitor">' + messageHtml + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + messageHtml + '</div>'
            }
          });

        const chatmessage = chat.querySelector('.chat__messages');
        chatmessage.innerHTML = html;
    }
}

const chat = new Chat();

chat.display();



// onSendButton(chat) {
//     var textField = chat.querySelector('input');
//     let text1 = textField.value;
//     if (text1 === "") {
//       return;
//     }

//     let msg1 = { name: "User", message: text1 };
//     this.messages.push(msg1);

//     this.sendMessage(text1, chat, textField);
//   }

//   sendMessage(message, chat, textField) {
//     fetch('http://127.0.0.1:5000/chat', {
//       method: 'POST',
//       body: JSON.stringify({ message: message }),
//       mode: 'cors',
//       headers: {
//         'Content-Type': 'application/json'
//       }
//     })
//     .then(r => r.json())
//     .then(response => {
//       let msg2 = { name: "Assistant", message: response.message };
//       this.messages.push(msg2);
//       this.updateChatText(chat);
//       textField.value = '';
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//       this.updateChatText(chat);
//       textField.value = '';
//     });
//   }