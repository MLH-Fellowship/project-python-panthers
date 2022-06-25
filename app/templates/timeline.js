// make sure to add onsubmit="postFormData(event)" to the form
async function postFormData(e) {
    // prevents going to the API return page
    e.preventDefault();

    // get form data
    const form = document.getElementById('timeline_form');
    const formData = new FormData(form);

    // try POST request
    try {
        await fetch('/api/timeline_post', {
            method: 'POST',
            body: formData
        })

    } catch (err) {
        console.log('An error occured');
    } finally {
        // reload
        form.reset()
        location.reload()
    }
}