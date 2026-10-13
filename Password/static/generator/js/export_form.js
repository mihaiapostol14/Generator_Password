document.addEventListener('DOMContentLoaded', function () {
  const exportForm = document.querySelector('#exportModal form')
  const exportModalElement = document.getElementById('exportModal')
  const mainPagePassword = document.querySelector('.show-password')
  const currentPassword = mainPagePassword.textContent.trim()

  if (!exportForm || !exportModalElement) return

  const exportModal = new bootstrap.Modal(exportModalElement)

  const exportTriggerBtn = document.getElementById('exportTriggerBtn')
  if (exportTriggerBtn) {
    exportTriggerBtn.addEventListener('click', () => {
      exportModal.show()
    })
  }

  // Pure Client-Side Export (No Django backend view required)
  exportForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const submitBtn = exportForm.querySelector('button[type="submit"]')
    const originalBtnText = submitBtn.innerHTML

    const formData = new FormData(exportForm)
    const fileFormat = formData.get('file_format') || 'txt'

    try {
      submitBtn.disabled = true
      submitBtn.innerHTML =
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Generating...'

      // Gather client-side data to export
      const exportData = {
        timestamp: new Date().toISOString(),
        password: currentPassword,
        generatedAt: window.location.href,
        content: mainPagePassword ? mainPagePassword.textContent.trim() : 'No password captured',
      }

      // Format data based on user selection (TXT or JSON)
      let fileContent = ''
      let mimeType = 'text/plain;charset=utf-8'

      if (fileFormat === 'json') {
        fileContent = JSON.stringify(exportData, null, 2)
        mimeType = 'application/json;charset=utf-8'
      } else {
        fileContent =
          `--- SECURE EXPORT DATA ---\n` +
          `Timestamp: ${exportData.timestamp}\n` +
          `Password: ${exportData.password}\n` +
          `Source: ${exportData.generatedAt}\n`
      }

      // Create client-side Blob and trigger download instantly
      const blob = new Blob([fileContent], { type: mimeType })
      const downloadUrl = window.URL.createObjectURL(blob)

      const dateStr = new Date().toISOString().slice(0, 10)
      const customFileName = `secure_export_${dateStr}.${fileFormat}`

      const a = document.createElement('a')
      a.href = downloadUrl
      a.download = customFileName
      document.body.appendChild(a)
      a.click()
      a.remove()
      window.URL.revokeObjectURL(downloadUrl)

      exportModal.hide()
      exportForm.reset()
    } catch (error) {
      console.error('Client-side export failed:', error)
      alert('An error occurred while generating the file.')
    } finally {
      submitBtn.disabled = false
      submitBtn.innerHTML = originalBtnText
    }
  })
})
