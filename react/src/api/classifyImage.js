import {userActions} from "../actions"

/**
 * Uploads an image of a flower and classifies it.
 * @param {Object} file The uploaded image
 */
export default async function classifyImage(file, token) {
  // Create payload
  const formData = new FormData();
  formData.append('file', file)

  let res = await fetch("/api/classification", {
    method: 'POST',
    body: formData,
    headers: {
      Authorization: `Bearer ${token}`
    }
  }).then(res => {
    if (res.status === 401) {
      userActions.logout();
      /* eslint-disable */
      location.reload();
    }
    return res.json();
  })

  return res;
}