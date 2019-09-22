import rootReducer from "../reducers";
import { configureStore } from "redux-starter-kit";


export default function configureAppStore(preloadedState) {
  const store = configureStore({
    reducer: rootReducer,
    preloadedState
  });

  return store;
}
