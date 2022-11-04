import { Dispatch } from "redux"
import { TodoAction } from "../../types/todoTypes"
import axios from 'axios'

import { fetchTodos, fetchTodosSuccess, fetchTodosError, setTodosPage } from "../reducers/todoReducer"

export const fetchTodosAction = (page = 1, limit = 10) => {
  return async (dispatch: Dispatch<TodoAction>) => {
    try {
      dispatch(fetchTodos())
      const response = await axios.get('https://jsonplaceholder.typicode.com/todos', {
        params: { _page: page, _limit: limit }
      })
      setTimeout(() => {
        dispatch(fetchTodosSuccess(response.data))
      }, 500);
    } catch (e) {
      dispatch(fetchTodosError('Error while loading todos'))
    }
  }
}

export function setTodoPage(page: number) {
  return (dispatch: Dispatch<TodoAction>) => dispatch(setTodosPage(page))
}