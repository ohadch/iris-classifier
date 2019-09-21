import {
    userConstants
} from '../constants';
import {
    userService
} from '../services';
import {
    alertActions
} from './';
import {
    history
} from '../helpers';

export const userActions = {
    login,
    logout
};

function login(username, password) {
    return async dispatch => {
        dispatch(request({
            username
        }));
        const {
            user,
            error
        } = await userService.login(username, password)

        if (error) {
            dispatch(failure(error));
            dispatch(alertActions.error(error));
            alert(error)
            return;
        } else {
            dispatch(success(user));
            history.push('/');
            /* eslint-disable */
            location.reload();
        }
    };

    function request(user) {
        return {
            type: userConstants.LOGIN_REQUEST,
            user
        }
    }

    function success(user) {
        return {
            type: userConstants.LOGIN_SUCCESS,
            user
        }
    }

    function failure(error) {
        return {
            type: userConstants.LOGIN_FAILURE,
            error
        }
    }
}

function logout() {
    userService.logout();
    return {
        type: userConstants.LOGOUT
    };
}