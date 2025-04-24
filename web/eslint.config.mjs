import { dirname } from 'path';
import { fileURLToPath } from 'url';
import { FlatCompat } from '@eslint/eslintrc';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends(
    'next/core-web-vitals',
    'next/typescript',
    'plugin:tailwindcss/recommended',
    'prettier',
  ),
  ...compat.config({
    plugins: ['@typescript-eslint', 'tailwindcss'],
    rules: {
      'tailwindcss/classnames-order': 'off',
    },
    parser: '@typescript-eslint/parser',
    overrides: [
      {
        files: ['*.ts', '*.tsx'],
        parserOptions: {
          project: './tsconfig.json',
          projectService: true,
          tsconfigRootDir: __dirname,
        },
        extends: [
          'next/core-web-vitals',
          'plugin:@typescript-eslint/recommended',
          'prettier',
        ],
        rules: {
          'tailwindcss/classnames-order': 'off',
        },
      },
    ],
  }),
];

export default eslintConfig;
