fetch('/api/timeline_post').then(response => {
            console.log(response);
            if (!response.ok){
                throw Error("ERROR");
            }
            return response.json();
        })
        .then(data => {
            console.log(data.timeline_posts);
            const html = data.timeline_posts.map(user => {
                return `
                <div class= "timeline-user"> 
                    <p>Name: ${user.name}</p>
                    <p>Email: ${user.email}</p>
                    <p>Content: ${user.content}</p>
                    </div>
            
                `;
            }).join('');
                console.log(html);
                document.querySelector("#app").insertAdjacentHTML("afterbegin", html);
        }).catch(error => {
            console.log(error);
        });
        const form = document.getElementById('timeline_form');
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const payload = new FormData(form);
           console.log([...payload])

            fetch('/api/timeline_post', {
                method: 'POST',
                body: payload,
            })
            
            // .then(res => res.json())
            
            .then(data => console.log(data))
            .catch(err => console.log(err))
            form.reset()
            location.reload()
        });
