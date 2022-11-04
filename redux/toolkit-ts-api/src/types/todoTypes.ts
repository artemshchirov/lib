export interface TodoState {
  todos: any[];
  loading: boolean;
  error: null | string;
  page: number;
  limit: number;
}

// export enum TodoActionTypes {
//   FETCH_TODOS = 'FETCH_TODOS',
//   FETCH_TODOS_SUCCESS = 'FETCH_TODOS_SUCCESS',
//   FETCH_TODOS_ERROR = 'FETCH_TODOS_ERROR',
//   SET_TODO_PAGE = 'SET_TODO_PAGE',
// }

interface FetchTodoAction {
  type: string;
}

interface FetchTodoSuccessAction {
  type: string;
  payload: any[];
}

interface FetchTodoErrorAction {
  type: string;
  payload: string;
}

interface SetTodoPage {
  type: string;
  payload: number;
}

export type TodoAction = FetchTodoAction | FetchTodoSuccessAction | FetchTodoErrorAction | SetTodoPage
