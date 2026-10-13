class PasswordOutput {
  constructor() {
    this.alertContainer = document.querySelector('.alert-success')
    this.passwordOutput = document.querySelector('.show-password')
    this.button = document.querySelector('.btn-copy')

    if (!this.passwordOutput || !this.button) return

    this.password = this.passwordOutput.textContent
    this.initTooltip()
    this.init()
  }

  initTooltip() {
    this.tooltip = bootstrap.Tooltip.getOrCreateInstance(this.button, {
      title: 'Copy password',
      trigger: 'hover focus',
      placement: 'top',
      customClass: 'custom-tooltip',
    })
  }

  init() {
    if (!this.password) {
      this.button.disabled = true
      return
    }

    this.addExportLink()
    this.bindCopyEvent()
  }

  addExportLink() {
    if (!this.alertContainer) return

    const exportLink = `
            <a href="#"
               class="alert-link"
               data-bs-toggle="modal"
               data-bs-target="#exportModal">
                Export
            </a>
        `

    this.alertContainer.insertAdjacentHTML('beforeend', exportLink)
  }

  bindCopyEvent() {
    this.button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(this.password)

        this.tooltip.setContent({
          '.tooltip-inner': 'Password copied!',
        })

        this.tooltip.show()

        setTimeout(() => {
          this.tooltip.setContent({
            '.tooltip-inner': 'Copy password',
          })
        }, 1500)
      } catch (error) {
        console.error('Failed to copy password:', error)
      }
    })
  }
}

// ADDED: Password strength meter class
class PasswordStrengthMeter {
  constructor() {
    this.passwordOutput = document.querySelector('.show-password')
    this.strengthBar = document.getElementById('passwordStrengthBar')
    this.strengthLabel = document.getElementById('passwordStrengthLabel')
    this.progress = this.strengthBar?.parentElement
  }

  evaluate(password) {
    if (!password) {
      return {
        score: 0,
        percentage: 0,
        color: 'bg-danger',
        label: '',
      }
    }

    const criteria = [
      password.length >= 8,
      password.length >= 12,
      /[a-z]/.test(password),
      /[A-Z]/.test(password),
      /[0-9]/.test(password),
      /[^a-zA-Z0-9]/.test(password),
    ]

    const score = criteria.filter(Boolean).length

    if (score <= 2) {
      return {
        score,
        percentage: 25,
        color: 'bg-danger',
        label: 'Weak',
      }
    }

    if (score <= 4) {
      return {
        score,
        percentage: 60,
        color: 'bg-warning',
        label: 'Medium',
      }
    }

    return {
      score,
      percentage: 100,
      color: 'bg-success',
      label: 'Strong',
    }
  }

  // ADDED: Call this after AJAX updates .show-password
  update(password) {
    if (!this.strengthBar || !this.strengthLabel || !this.progress) return

    const result = this.evaluate(password)

    this.strengthBar.style.width = `${result.percentage}%`
    this.strengthBar.classList.remove('bg-danger', 'bg-warning', 'bg-success')
    this.strengthBar.classList.add(result.color)

    this.strengthLabel.textContent = result.label
    this.progress.setAttribute('aria-valuenow', result.percentage)
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new PasswordOutput()

  // ADDED: Initialize the password strength meter
  window.passwordStrengthMeter = new PasswordStrengthMeter()

  // ADDED: Evaluate the initial password on page load
  const passwordOutput = document.querySelector('.show-password')
  if (passwordOutput) {
    window.passwordStrengthMeter.update(passwordOutput.textContent)
  }
})
