/**
 * Uploads an image of a flower and classifies it.
 * @param {Object} file The uploaded image
 */
export default async function classifyImage(file) {
    // Create payload
    const formData = new FormData();
    formData.append('file', file)

    return fetch("/api/file", {
        method: 'POST',
        body: formData
      }).then(res => res.json())
}