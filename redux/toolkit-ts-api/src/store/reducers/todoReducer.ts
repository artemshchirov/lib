import { createSlice } from '@reduxjs/toolkit';
import { PayloadAction } from '@reduxjs/toolkit'
import { TodoState } from '../../types/todoTypes';

const initialState = {
  todos: [],
  loading: false,
  error: null,
  page: 1,
  limit: 10
} as TodoState

const todoReducer = createSlice({
  name: 'user',
  initialState,
  reducers: {
    fetchTodos: (state) => {
      return { ...state, loading: true }
    },
    fetchTodosSuccess: (state, action: PayloadAction<any[]>) => {
      return { ...state, loading: false, todos: action.payload }
    },
    fetchTodosError: (state, action: PayloadAction<string>) => {
      return { ...state, loading: false, error: action.payload }
    },
    setTodosPage: (state, action: PayloadAction<number>) => {
      return { ...state, page: action.payload }
    },
  },
});

export const { fetchTodos, fetchTodosSuccess, fetchTodosError, setTodosPage } = todoReducer.actions;
export default todoReducer.reducer;
