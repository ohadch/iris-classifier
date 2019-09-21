import { combineReducers } from 'redux';

import { authentication } from './authentication.reducer';
import { alert } from './alert.reducer';
import { images } from './images.reducer';

const rootReducer = combineReducers({
  authentication,
  alert,
  images
});

export default rootReducer;