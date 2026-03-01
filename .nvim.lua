-- OSGeo Hugo Website nvim project configuration
-- Auto-sourced by nvim when exrc is enabled, or source manually with:
--   :source .nvim.lua
--
-- Workflow:
--   1. Start Hugo dev server: <leader>ps (or :HugoServer)
--   2. Open browser: <leader>po
--   3. Edit content, preview changes
--   4. Format files: <leader>pf
--   5. Build for production: <leader>pb

-- Guard against re-sourcing
if vim.g.osgeo_hugo_loaded then
  return
end
vim.g.osgeo_hugo_loaded = true

-- Helper function for terminal commands
local function run_in_terminal(cmd, desc)
  return function()
    vim.cmd('terminal ' .. cmd)
    vim.notify('OSGeo Hugo: ' .. desc, vim.log.levels.INFO)
  end
end

-- Helper function for shell commands
local function run_shell(cmd, desc)
  return function()
    vim.cmd('!' .. cmd)
    vim.notify('OSGeo Hugo: ' .. desc, vim.log.levels.INFO)
  end
end

-- ============================================================================
-- User Commands
-- ============================================================================

-- Hugo commands
vim.api.nvim_create_user_command('HugoServer', function()
  vim.cmd('terminal hugo server --config config.toml,config/config.dev.toml')
end, { desc = 'Start Hugo development server' })

vim.api.nvim_create_user_command('HugoServerDrafts', function()
  vim.cmd('terminal hugo server --config config.toml,config/config.dev.toml --buildDrafts')
end, { desc = 'Start Hugo server with drafts' })

vim.api.nvim_create_user_command('HugoBuild', function()
  vim.cmd('!hugo --config config.toml,config/config.dev.toml')
end, { desc = 'Build site (development)' })

vim.api.nvim_create_user_command('HugoBuildProd', function()
  vim.cmd('!make build')
end, { desc = 'Build site (production)' })

vim.api.nvim_create_user_command('HugoNew', function(opts)
  if opts.args ~= '' then
    vim.cmd('!hugo new ' .. opts.args)
  else
    vim.notify('Usage: :HugoNew <path/to/content.md>', vim.log.levels.WARN)
  end
end, { nargs = '?', desc = 'Create new content' })

-- Formatting commands
vim.api.nvim_create_user_command('PrettierFormat', function()
  local file = vim.fn.expand('%')
  vim.cmd('!npx prettier --write ' .. file)
  vim.cmd('edit!')
end, { desc = 'Format current file with Prettier' })

vim.api.nvim_create_user_command('PrettierFormatAll', function()
  vim.cmd('!npx prettier --write "content/**/*.md" "themes/**/*.html" "themes/**/*.css"')
end, { desc = 'Format all content and theme files' })

vim.api.nvim_create_user_command('PrettierCheck', function()
  vim.cmd('!npx prettier --check "content/**/*.md" "themes/**/*.html"')
end, { desc = 'Check formatting with Prettier' })

-- Linting commands
vim.api.nvim_create_user_command('MarkdownLint', function()
  vim.cmd('!npx markdownlint-cli "content/**/*.md"')
end, { desc = 'Lint Markdown files' })

vim.api.nvim_create_user_command('HtmlHint', function()
  vim.cmd('!npx htmlhint "public/**/*.html"')
end, { desc = 'Lint HTML output' })

-- Git/Pre-commit commands
vim.api.nvim_create_user_command('PreCommit', function()
  vim.cmd('!pre-commit run --all-files')
end, { desc = 'Run pre-commit hooks' })

vim.api.nvim_create_user_command('GitStatus', function()
  vim.cmd('!git status')
end, { desc = 'Show git status' })

vim.api.nvim_create_user_command('GitDiff', function()
  vim.cmd('terminal git diff')
end, { desc = 'Show git diff' })

-- Make commands
vim.api.nvim_create_user_command('Make', function(opts)
  if opts.args ~= '' then
    vim.cmd('!make ' .. opts.args)
  else
    vim.cmd('!make help')
  end
end, { nargs = '?', desc = 'Run make command' })

vim.api.nvim_create_user_command('MakeBuild', function()
  vim.cmd('!make build')
end, { desc = 'Run make build' })

vim.api.nvim_create_user_command('MakeDev', function()
  vim.cmd('terminal make hugo-run-dev')
end, { desc = 'Run make hugo-run-dev' })

-- Utility commands
vim.api.nvim_create_user_command('OpenBrowser', function()
  vim.cmd('!xdg-open http://localhost:1313 2>/dev/null || open http://localhost:1313')
end, { desc = 'Open site in browser' })

vim.api.nvim_create_user_command('NixDevelop', function()
  vim.cmd('terminal nix develop')
end, { desc = 'Enter Nix development shell' })

vim.api.nvim_create_user_command('CleanPublic', function()
  vim.cmd('!rm -rf public public_dev public_prod public_www')
  vim.notify('Cleaned public directories', vim.log.levels.INFO)
end, { desc = 'Clean build output directories' })

-- Content helpers
vim.api.nvim_create_user_command('NewPage', function(opts)
  if opts.args ~= '' then
    vim.cmd('!hugo new ' .. opts.args .. '/_index.md')
    vim.cmd('edit content/' .. opts.args .. '/_index.md')
  else
    vim.notify('Usage: :NewPage <section/path>', vim.log.levels.WARN)
  end
end, { nargs = '?', desc = 'Create new section page' })

vim.api.nvim_create_user_command('NewPost', function(opts)
  local title = opts.args ~= '' and opts.args or 'new-post'
  local slug = title:lower():gsub('%s+', '-'):gsub('[^%w%-]', '')
  local path = 'news/' .. os.date('%Y-%m-%d') .. '-' .. slug .. '.md'
  vim.cmd('!hugo new ' .. path)
  vim.cmd('edit content/' .. path)
end, { nargs = '?', desc = 'Create new news post' })

-- ============================================================================
-- Which-Key Registration
-- ============================================================================

local wk_ok, wk = pcall(require, 'which-key')
if wk_ok then
  wk.add({
    -- Project group
    { '<leader>p', group = 'Project (OSGeo Hugo)' },

    -- Hugo server & build
    { '<leader>ps', '<cmd>HugoServer<cr>', desc = 'Start Hugo server' },
    { '<leader>pS', '<cmd>HugoServerDrafts<cr>', desc = 'Hugo server (with drafts)' },
    { '<leader>pb', '<cmd>HugoBuild<cr>', desc = 'Build site (dev)' },
    { '<leader>pB', '<cmd>HugoBuildProd<cr>', desc = 'Build site (prod)' },
    { '<leader>po', '<cmd>OpenBrowser<cr>', desc = 'Open in browser' },

    -- Formatting
    { '<leader>pf', '<cmd>PrettierFormat<cr>', desc = 'Format current file' },
    { '<leader>pF', '<cmd>PrettierFormatAll<cr>', desc = 'Format all files' },

    -- Linting
    { '<leader>pl', '<cmd>MarkdownLint<cr>', desc = 'Lint Markdown' },
    { '<leader>pL', '<cmd>HtmlHint<cr>', desc = 'Lint HTML output' },
    { '<leader>pc', '<cmd>PrettierCheck<cr>', desc = 'Check formatting' },

    -- Pre-commit / Git
    { '<leader>pp', '<cmd>PreCommit<cr>', desc = 'Run pre-commit' },
    { '<leader>pg', '<cmd>GitStatus<cr>', desc = 'Git status' },
    { '<leader>pd', '<cmd>GitDiff<cr>', desc = 'Git diff' },

    -- Make commands
    { '<leader>pm', '<cmd>Make<cr>', desc = 'Make (show help)' },
    { '<leader>pM', '<cmd>MakeDev<cr>', desc = 'Make dev server' },

    -- Content creation
    { '<leader>pn', '<cmd>NewPost<cr>', desc = 'New news post' },
    { '<leader>pN', '<cmd>NewPage<cr>', desc = 'New section page' },

    -- Utilities
    { '<leader>px', '<cmd>NixDevelop<cr>', desc = 'Nix develop shell' },
    { '<leader>pC', '<cmd>CleanPublic<cr>', desc = 'Clean build dirs' },
  })
else
  -- Fallback keymaps if which-key not available
  local opts = { noremap = true, silent = true }

  -- Hugo
  vim.keymap.set('n', '<leader>ps', '<cmd>HugoServer<cr>', vim.tbl_extend('force', opts, { desc = 'Start Hugo server' }))
  vim.keymap.set('n', '<leader>pb', '<cmd>HugoBuild<cr>', vim.tbl_extend('force', opts, { desc = 'Build site' }))
  vim.keymap.set('n', '<leader>po', '<cmd>OpenBrowser<cr>', vim.tbl_extend('force', opts, { desc = 'Open in browser' }))

  -- Formatting
  vim.keymap.set('n', '<leader>pf', '<cmd>PrettierFormat<cr>', vim.tbl_extend('force', opts, { desc = 'Format file' }))

  -- Linting
  vim.keymap.set('n', '<leader>pl', '<cmd>MarkdownLint<cr>', vim.tbl_extend('force', opts, { desc = 'Lint Markdown' }))

  -- Pre-commit
  vim.keymap.set('n', '<leader>pp', '<cmd>PreCommit<cr>', vim.tbl_extend('force', opts, { desc = 'Pre-commit' }))
end

-- ============================================================================
-- Auto-commands
-- ============================================================================

-- Auto-format Markdown on save (optional, uncomment to enable)
-- vim.api.nvim_create_autocmd('BufWritePre', {
--   pattern = '*.md',
--   callback = function()
--     vim.cmd('silent! PrettierFormat')
--   end,
-- })

-- Set filetypes for Hugo templates
vim.api.nvim_create_autocmd({ 'BufRead', 'BufNewFile' }, {
  pattern = { '*.html' },
  callback = function()
    -- Check if we're in a Hugo project
    if vim.fn.filereadable('config.toml') == 1 then
      vim.bo.filetype = 'gohtmltmpl'
    end
  end,
})

-- ============================================================================
-- Notification
-- ============================================================================

vim.notify("OSGeo Hugo: Project config loaded. Use <leader>p for commands.", vim.log.levels.INFO)
