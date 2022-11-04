import { combineReducers } from '@reduxjs/toolkit'
import { configureStore } from '@reduxjs/toolkit'
import userReducer from './reducers/UserSlice'

const rootReducer = combineReducers({
  userReducer
})

export const setupStore = () => {
  return configureStore({
    reducer: rootReducer
  })
}

export type RootState = ReturnType<typeof rootReducer>
export type AppStore = ReturnType<typeof setupStore>
export type AppDispatch = AppStore['dispatch']

console.log('rootReducer: ', combineReducers({
}));
console.log('configureStore: ', configureStore({
  reducer: rootReducer
}));
console.log('================');
