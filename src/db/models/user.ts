import { DataTypes, Model, Optional } from 'sequelize';
import sequelizeConnection from '../../config.js';

interface UserAttributes {
    id: number;
    slug: string;
    firstName: string;
    lastName: string;
    email: string;
    password: string;
    createdAt?: Date;
    updatedAt?: Date;
    deletedAt?: Date;
}
export interface UserInput extends Optional<UserAttributes, 'id' | 'slug'> {}
export interface UserOutput extends Required<UserAttributes> {}


class User extends Model<UserAttributes, UserInput> implements UserAttributes {
    public id!: number;
    public slug!: string;
    public firstName!: string;
    public lastName!: string;
    public email!: string;
    public password!: string;
    public readonly createdAt!: Date;
    public readonly updatedAt!: Date;
    public readonly deletedAt!: Date;
}

User.init({
    id: {
        type: DataTypes.INTEGER.UNSIGNED,
        autoIncrement: true,
        primaryKey: true,
    }, 
    firstName: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    lastName: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    slug: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true,
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true,
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false,
    },
}, {
    timestamps: true,
    sequelize: sequelizeConnection,
    paranoid: true,
})

export default User;