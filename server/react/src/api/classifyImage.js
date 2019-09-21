/**
 * Uploads an image of a flower and classifies it.
 * @param {Object} file The uploaded image
 */
export default async function classifyImage(file, token) {
    // Create payload
    const formData = new FormData();
    formData.append('file', file)

    return fetch("/api/classification", {
        method: 'POST',
        body: formData,
        headers: {
          Authorization: `Bearer ${token}`
        }
      }).then(res => res.json())
}
