function lanjut(halaman){
	// Get the modal
	if (halaman == 'profil'){
		$('#' + halaman).css('display', 'none');
		$('#pesan').css('display', 'block');
		$('#orang').removeClass('active');
		$('#surat').attr('class', 'active');
	}else if (halaman == 'pesan'){
		$('#' + halaman).css('display', 'none');
		$('#sandi').css('display', 'block');
		$('#surat').removeClass('active');
		$('#bulat').attr('class', 'active');
	}else{
		$('#' + halaman).css('display', 'none');
		$('#selamat').css('display', 'block');
		$('#bulat').removeClass('active');
		$('#atas').attr('class', 'active');
	}
}