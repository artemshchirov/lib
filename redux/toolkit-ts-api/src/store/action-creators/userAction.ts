import { Dispatch } from "redux"
import { UserAction } from "../../types/userTypes"
import axios from 'axios'

import { fetchUsers, fetchUsersSuccess, fetchUsersError } from "../reducers/userReducer"

export const fetchUsersAction = () => {
  return async (dispatch: Dispatch<UserAction>) => {
    try {
      dispatch(fetchUsers())
      const response = await axios.get('https://jsonplaceholder.typicode.com/users')
      setTimeout(() => {
        dispatch(fetchUsersSuccess(response.data))
      }, 500);
    } catch (e) {
      dispatch(fetchUsersError('Error while loading users data'))
    }
  }
}