const images = (state = [], action) => {
    switch (action.type) {
      case 'ADD_IMAGE':
        return [
          ...state,
          ...action.image
        ]
      case 'CLASSIFY_IMAGE':
        return state.map(image =>
          (image.id === action.id)
            ? {...image, classification: action.classification}
            : image
        )
      default:
        return state
    }
  }
  
  export default images