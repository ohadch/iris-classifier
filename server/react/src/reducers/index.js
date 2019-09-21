import { combineReducers } from 'redux';

import { authentication } from './authentication.reducer';
import { users } from './users.reducer';
import { alert } from './alert.reducer';
import { images } from './images.reducer';

const rootReducer = combineReducers({
  authentication,
  users,
  alert,
  images
});

export default rootReducer;